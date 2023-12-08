# import pytest

# from contextlib import nullcontext as does_not_raise

# from mailing.routers import get_list_reports_for_subscription
import pytest

from config.config import Base, engine, settings


# @pytest.fixture(scope='session', autouse=True)
# def setup_db():
#     print(f"{settings.MODE}")
#     assert settings.MODE == 'Test'
#     Base.metadata.create_all(engine)
#     yield
#     Base.metadata.drop_all(engine)


class ReportRouterTest:
    # @pytest.mark.parametrize(
    #     "res, expectation",
    #     [
    #         ([
    #         "Опорные филиалы",
    #         "Прибыли и убытки РТК",
    #         "РТК+Tele2",
    #         "Сегмантная отчетность"
    #         ], does_not_raise())
    #     ]
    # )
    # def test_get_list_reports_for_subscription(self, res, expectation):
    #     # with expectation:
    #     assert get_list_reports_for_subscription() == res
    pass



    # with pytest.raises(TypeError):
    #     assert get_list_reports_for_subscription()

def test_dev():
    assert 1 == 1