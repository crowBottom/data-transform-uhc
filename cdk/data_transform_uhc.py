import builtins
import aws_cdk
from aws_cdk import (
    aws_iam as iam,
    aws_s3 as s3,
    aws_events,
    aws_lambda as _lambda,
    aws_s3_notifications as s3_notify,
    aws_stepfunctions as _aws_stepfunctions,
    aws_stepfunctions_tasks as tasks,
    aws_events_targets as targets,
    aws_lambda_event_sources as eventsources,
    Duration
)

import constructs
from cdk.build_config import BuildConfig

class DataTransformUHC(aws_cdk.Stack):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        config: BuildConfig,
        *args,
        **kwargs
    ):

        super().__init__(scope, id, *args, **kwargs)

        # Define stack resources below

        uhc_data_transform_lambda = _lambda.Function(
            scope=self,
            id="uhc-data-transform-lambda",
            handler="lambda_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('events/uhc_data_transform')
        )
