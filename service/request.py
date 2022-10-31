from core.config import IMAP_SERVER, IMAP_PASSWORD, IMAP_EMAIL
from imap_tools import MailBox, A
from datetime import datetime, timedelta
from core.constant import EMPLOYMENT, FILTER_MAIL
from core.db import getDb
from sqlalchemy.orm import Session
from model.request import Request
from sqlalchemy import insert


class RequestService:
    def __init__(self, ):
        self.imap = MailBox(IMAP_SERVER)
        self.imap.login(IMAP_EMAIL, IMAP_PASSWORD)
        self.session: Session = next(getDb())

    @property
    def tools(self):
        try:
            mails = self.imap.fetch(A(from_=FILTER_MAIL))
            message = next(mails)
            message_content = message.text.split('\n')
            message_date = message.date
            location, subject = self.getSubject(message_content[12])
            content_list = self.getContentList(message_content[13:len(message_content) - 19], subject, location, message_date)
            self.imap.delete(message.uid)
            return content_list, message.uid
        except Exception:
            ...

    def getContentList(self, content: list, subject: str, location: str, request_date: datetime) -> list:
        start = 0
        list_content = []
        while start + 5 < len(content):
            try:
                location_and_company_name = content[start + 2].split('-')
                request = {
                    "subject": subject,
                    "location": location,
                    "companyLocation": location_and_company_name[len(location_and_company_name) - 1],
                    "companyName": location_and_company_name[0],
                    "createdDate": datetime.now(),
                    "requestDate": request_date,
                    "title": content[start + 1],
                    "url": content[start + 5]
                }
                list_content.append(request)
                self.createRequest(**request)
                start = content.index("", start + 1, len(content))
            except ValueError:
                break
        return list_content

    @staticmethod
    def getSubject(subject: list) -> tuple:
        subject_list = subject.split(" ")
        index_employment = subject_list.index(EMPLOYMENT)
        try:
            index_lodash = subject_list.index("-")
            return " ".join(subject_list[index_lodash + 1:len(subject_list)]), " ".join(
                subject_list[index_employment + 1: index_lodash])
        finally:
            return " ", " ".join(subject_list[index_employment + 1:len(subject_list)])

    def createRequest(self, **args: Request):
            stmt = insert(Request).values(args)
            self.session.execute(stmt)
            self.session.commit()
    async def get_yesterday_request(self):
        return self.session.query(Request).filter(Request.createdDate.between(datetime.now()-timedelta(days=1), datetime.now())).all()

    async def get_request(self, start: datetime, end: datetime):
        return self.session.query(Request).filter(Request.createdDate.between(start, end)).all()


def generateRequest():
    service = RequestService()
    yield service.tools
