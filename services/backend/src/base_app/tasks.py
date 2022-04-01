from celery import Task as CeleryTask
from celery.result import AsyncResult
from dsp.celery import app
from ws_app.consts import WS_TASK_READY_EVENT_KEY
from ws_app.utils import send_ws_notification_to_groups


class SendTaskResultTask(CeleryTask):
    name = 'send_task_result_task'

    def run(self, *args, task_id='', group_name=''):
        task_result = AsyncResult(task_id)
        send_ws_notification_to_groups(
                [group_name],
                WS_TASK_READY_EVENT_KEY,
                {
                    'task_id': task_result.task_id,
                    'status': task_result.status,
                    'result': task_result.result,
                }
            )
        return task_result.status


app.register_task(SendTaskResultTask)
