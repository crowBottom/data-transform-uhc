import os
import aws_cdk
import cdk

app = aws_cdk.App()

# dev stack

cdk.DataTransformUHC(
    app,
    "data-transform-uhc-dev",
    env=aws_cdk.Environment(account="221278850141", region="us-east-1"),
    description="Data transform uhc dev environment",
    tags={
        "Application": "Data transform uhc application",
        "Environment": "dev",
        "Version": os.environ.get("VERSION")
    },
    config=cdk.BuildConfig(**app.node.try_get_context("dev"))
)

app.synth()
