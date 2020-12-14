from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.core import Stack

from b_twilio_sdk_layer.layer import Layer as TwilioLayer


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'TestingStack',
            stack_name=f'TestingStack'
        )

        Function(
            scope=self,
            id='TestingFunction',
            code=Code.from_inline(
                'def handler(): return "Hello World!"'
            ),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            layers=[TwilioLayer(self, 'TestingTwilioLayer', boto3_version='1.16.35')]
        )
