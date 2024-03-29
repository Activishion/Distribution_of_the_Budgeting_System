import random

from fastapi import HTTPException

from config.logging import error_log
from config.utils import InterfaseContextManager
from .schemas import (CreateSubscriptionNewReport, CreateSubscriptionOnMessages,
                      ReadReports30Day)


class MessageService:
    async def get_all_messages(self, cmd: InterfaseContextManager):
        async with cmd: # pattern unit of work
            response_alchemy = await cmd.message.find_all()

            # The data after alchemy has its own format and must be converted 
            # into Python format either manually or using the method modal_validate from pydantic
            response_list: list = []
            for response in response_alchemy: 
                dict = {
                    'id': str(response.id),
                    'send_date': str(response.send_date),
                    'author': response.author,
                    'external_users': response.external_users,
                    'internal_users': response.internal_users,
                    'subject': response.subject,
                    'html_body': response.html_body,
                    'plain_body': response.plain_body,
                }
                response_list.append(dict)

            if len(response_list) == 0:
                error_log.error('Error loading messages.')
                raise HTTPException(status_code=404, detail='Error loading messages.')
            return response_list

    async def get_message_by_id(self, id: str, cmd: InterfaseContextManager):
        if len(id) < 32 or len(id) > 36: 
            error_log.error('Error format uuid.')
            raise HTTPException(status_code=400, detail='Error format uuid.')

        async with cmd:
            response_alchemy = await cmd.message.find_one_by_id(id)

            if response_alchemy is None:
                error_log.error('Error loading data.')
                raise HTTPException(status_code=500, detail='Error loading data.')

            return {
                'id': str(response_alchemy.id),
                'send_date': str(response_alchemy.send_date),
                'author': response_alchemy.author,
                'external_users': response_alchemy.external_users,
                'internal_users': response_alchemy.internal_users,
                'subject': response_alchemy.subject,
                'html_body': response_alchemy.html_body,
                'plain_body': response_alchemy.plain_body,
            }
        
    async def create_subscription_on_information_messages(
        self,
        report_on_new: CreateSubscriptionOnMessages,
        cmd: InterfaseContextManager
    ):
        async with cmd:
            report_dict_on_news = report_on_new.model_dump() # serialization in python

            if report_dict_on_news.get('subscription') == 'Подписаться':
                news_subscription = await cmd.report.return_add_state_through_procedures(
                    report_dict_on_news['email'],
                    report_dict_on_news['author']
                )
                if news_subscription is None:
                    await cmd.rollback()
                    return None

                await cmd.commit()
                return news_subscription
            elif report_dict_on_news.get('subscription') == 'Отписаться':
                unsubscribe_from_news = await cmd.report.return_delete_state_through_procedures(
                    report_dict_on_news['email']
                )

                if unsubscribe_from_news is None:
                    await cmd.rollback()
                    return None

                await cmd.commit()
                return unsubscribe_from_news


class ReportService:
    async def create_subscription_on_report(
        self,
        report: CreateSubscriptionNewReport,
        cmd: InterfaseContextManager
    ):
        async with cmd:
            subscription_dict = report.model_dump()

            report_id = await cmd.report.get_report_by_report_name(subscription_dict['report'])

            if subscription_dict.get('subscription') == 'Подписаться':
                response_add = await cmd.report.add_one_user_through_procedures(subscription_dict['email'], report_id)

                if response_add is None:
                    await cmd.rollback()
                    return None

                await cmd.commit()
                return response_add
            elif subscription_dict.get('subscription') == 'Отписаться':
                response_delete = await cmd.report.delete_user_through_procedures(subscription_dict['email'], report_id)

                if response_delete is None:
                    await cmd.rollback()
                    return None

                await cmd.commit()
                return response_delete

    async def check_subscription(self, email: str, cmd: InterfaseContextManager):
        async with cmd:
            email_body = email.model_dump()
            user_verification = await cmd.report.check_user(email_body['email'])
            
            if user_verification is None:
                error_log.error('User not found.')
                raise HTTPException(status_code=404, detail='User not found.')

            response = await cmd.report.check_subscription(user_verification.email)

            if response.email is None:
                error_log.error('User not subscription.')
                raise HTTPException(status_code=404, detail='User not subscription.')

            if response.moderator_acc == True and response.date_deleted is None:
                return True
            return False

    async def get_report_by_email(self, email: str, cmd: InterfaseContextManager):
        async with cmd:
            report = await cmd.report.find_one_by_email(email)

            if report is None:
                error_log.error('Report not found.')
                raise HTTPException(status_code=404, detail='Report not found.')
            
            return {
                'email': report.email,
                'user_name': report.user_name,
                'date_added': str(report.date_added),
                'self_add': report.self_add,
                'date_deleted': str(report.date_deleted),
                'moderator_acc': report.moderator_acc,
                'moderator_name': report.moderator_name,
                'acc_date': str(report.acc_date),
                'sym_name': report.sym_name,
                'external_flg': report.external_flg,
                'moderator_comm': report.moderator_comm,
                'moderator_name_del': report.moderator_name_del,
                'moderator_comm_del': report.moderator_comm_del
            }

    async def get_all_reports(self, cmd: InterfaseContextManager):
        async with cmd:
            response_alchemy = await cmd.report.subscription_in_30_days()

            if response_alchemy is None:
                error_log.error('Reports not found.')
                raise HTTPException(status_code=404, detail='Reports not found.')

            # transformation of data to output format
            response_list: list = []
            response_keys: tuple = ('date_x', 'date', 'op', 'email', 'user_name', 'state')
            for response in response_alchemy:
                response_dict = dict(zip(response_keys, response))
                del response_dict["date_x"]
                response_dict["id"] = random.randint(1, 1000000000000)
                response_list.append(response_dict)
            
            return [ReadReports30Day.model_validate(response).dict() for response in response_list] # serialization from python
        
    async def get_list_reports_for_subscription(self, cmd: InterfaseContextManager):
        async with cmd:
            response_alchemy = await cmd.report.get_list_reports()

            if response_alchemy is None:
                error_log.error('Reports for subscription not found.')
                raise HTTPException(status_code=404, detail='Reports for subscription not found.')
            
            return list(response_alchemy.values())
        