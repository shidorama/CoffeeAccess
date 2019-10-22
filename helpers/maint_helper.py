import datetime

from consts.maintenance_type import MaintenanceType


def get_default_m_time(m_type: MaintenanceType):
    current_time = datetime.datetime.now()
    m_today: datetime.datetime
    if m_type == MaintenanceType.MORNING:
        m_today = get_mm_for_date(current_time)
    else:
        m_today = get_em_for_date(current_time)
    m_tmrw = m_today + datetime.timedelta(days=1)
    if current_time > m_today:
        return m_tmrw
    return m_today


def get_mm_for_date(date: datetime.datetime):
    return date.replace(hour=6, minute=0, second=0, microsecond=0)


def get_em_for_date(date: datetime.datetime):
    return date.replace(hour=17, minute=0, second=0, microsecond=0)
