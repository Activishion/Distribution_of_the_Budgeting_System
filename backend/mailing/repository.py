from abc import  abstractmethod, ABC

from sqlalchemy import text #Eliminates injections, required

from config.logging import error_log
from config.repository import SQLAlchemyRepository
from mailing.models import Reporting, Message


class MessageRepository(SQLAlchemyRepository, ABC):
    model = Message


class AbstractReportRepository(SQLAlchemyRepository, ABC):
    """ 
    Repository interface for reports.
    """
    @abstractmethod
    async def add_one_user_through_procedures():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_user_through_procedures():
        raise NotImplementedError
    
    @abstractmethod
    async def return_delete_state_through_procedures():
        raise NotImplementedError
    
    @abstractmethod
    async def return_add_state_through_procedures():
        raise NotImplementedError
    
    @abstractmethod
    async def subscription_in_30_days():
        raise NotImplementedError
    
    @abstractmethod
    async def get_list_reports():
        raise NotImplementedError
    
    @abstractmethod
    async def get_report_by_report_name():
        raise NotImplementedError
    

class ReportingRepository(AbstractReportRepository):
    model = Reporting

    async def add_one_user_through_procedures(self, email: str, report_id: str):
        """
            Add a user subscription to the specified report.
            :param email: email of the subscriber
            :param report_id: report to which subscription is made
        """
        stmt = (text(
            f"call bi.np_add_new_user_web({email}::varchar, {report_id}::varchar, ''::varchar, 0::int2)"
        ))
        try:
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except:
            error_log.error('Procedure call error: bi.np_add_new_user_web.')
            return None
    
    async def delete_user_through_procedures(self, email: str, report_id: str):
        """
            Delete a user subscription to the specified report.
            :param email: email of the subscriber
            :param report_id: report to which subscription is made
        """
        stmt = (text(
            f"call bi.np_delete_new_user_web({email}::varchar, {report_id}::varchar, ''::varchar, 0::int2)"
        ))
        try:
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except:
            error_log.error('Procedure call error: bi.np_delete_new_user_web.')
            return None
    
    async def return_delete_state_through_procedures(self, email: str):
        """
            Remove a user's news subscription.
            :param email: email of the subscriber
        """
        stmt = (text(
            f"call huml.delete_user({email}, 'Портал', 'Удален по собственному желанию', true, ''::varchar, 0::int2)"
        ))
        try:
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except:
            error_log.error('Procedure call error: huml.delete_user.')
            return None
    
    async def return_add_state_through_procedures(self, email: str, user_name: str):
        """
            Subscribe the user to news.
            :param email: email of the subscriber
            :param user_name: name of the subscriber
        """
        stmt = (text(
            f"call huml.add_user({email}, {user_name}, true, ''::varchar, 0::int2)"
        ))
        try:
            result = await self.session.execute(stmt)
            return result.scalar_one()
        except:
            error_log.error('Procedure call error: huml.add_user.')
            return None

    async def subscription_in_30_days(self):
        query = (text(
            "SELECT date_T, to_char(date_t, 'DD.MM.YY HH24:MI') date_t2, op, LEFT(email, 32) email, LEFT(user_name, 33) user_name, stat " 
            "FROM ("
            	"SELECT date_added date_T, 'Включение' op, " 
            	"CASE WHEN moderator_acc IS null " 
            	"THEN 'Ожидает' WHEN moderator_acc THEN 'Согласовано' ELSE 'Отклонено' " 
            	"END stat, email, user_name " 
                "FROM huml.mailing_list WHERE date_added between now()-interval '30 days' and now() " 
            	"UNION ALL SELECT date_deleted date_t, 'Исключение' op, " 
            	"CASE WHEN moderator_acc IS null THEN 'Ожидает' WHEN moderator_acc THEN 'Согласовано' ELSE 'Отклонено' END stat, email, user_name " 
                "FROM huml.mailing_list WHERE date_deleted between now()-interval '30 days' AND now() "
            ") a ORDER BY 1 desc"
        ))
        try:
            result = await self.session.execute(query)
            return result.fetchall()
        except:
            error_log.error('Error requesting subscription history.')
            return None

    async def get_list_reports(self):
        query = (text(
            "SELECT Report_ID, Report_Name "
            "FROM bi.NP_Reports "
            "WHERE Is_Public "
            "ORDER BY 2"
        ))
        try:
            result = await self.session.execute(query)
            return dict(result.fetchall())
        except:
            error_log.error('Error in request to get list of reports.')
            return None
    
    async def get_report_by_report_name(self, report_id: str):
        query = (text(
            "SELECT Report_ID "
            "FROM bi.NP_Reports "
           f"WHERE Report_Name = '{report_id}';"
        ))
        try:
            result = await self.session.execute(query)
            return result.scalar_one_or_none()
        except:
            error_log.error('Receive report request failed.')
            return None
