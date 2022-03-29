from fourier_transform_app.models import FourierTransformResult
from ws_app.consumers.celery_result import CeleryResultConsumer


class FourierTransformResultConsumer(CeleryResultConsumer):
    def connect(self):
        self.create_username_group()
        self.accept()
        task_id = self.scope['url_route']['kwargs']['task_id']
        self.send_task_result(FourierTransformResult, task_id)

    def receive_json(self, content, **kwargs):
        task_id = content.get('task_id', '')
        self.send_task_result(FourierTransformResult, task_id)
