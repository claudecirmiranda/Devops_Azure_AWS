from diagrams import Diagram, Group
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.devtools import Codecommit, Codebuild, Codedeploy, Codepipeline
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.azure.compute import AppServices, AKS
from diagrams.azure.database import SQLDatabases
from diagrams.azure.devops import Devops
from diagrams.azure.network import LoadBalancers
from diagrams.azure.storage import StorageAccounts
import graphviz as gv

with Diagram("AWS and Azure DevOps Solution", show=False):
    with Group("AWS DevOps"):
        with Group("Source Code Management"):
            aws_source = Codecommit("CodeCommit")

        with Group("Build and Test"):
            aws_build = Codebuild("CodeBuild")

        with Group("Deployment"):
            aws_deploy = Codedeploy("CodeDeploy")
            aws_autoscaling = EC2("Auto Scaling Group")
            aws_elb = ELB("ELB")

        with Group("Infrastructure"):
            aws_ec2 = EC2("EC2 instances")
            aws_rds = RDS("RDS Database")
            aws_s3 = S3("S3 Bucket")

        aws_pipeline = Codepipeline("CodePipeline")

        aws_source >> aws_pipeline
        aws_pipeline >> aws_build >> aws_deploy >> aws_autoscaling
        aws_autoscaling >> aws_ec2
        aws_ec2 >> aws_elb
        aws_rds >> aws_ec2
        aws_s3 >> aws_ec2

    with Group("Azure DevOps"):
        with Group("Source Code Management"):
            azure_source = Devops("Azure Repos")

        with Group("Build and Test"):
            azure_build = Devops("Azure Pipelines")

        with Group("Deployment"):
            azure_deploy = Devops("Azure Deployment Slots")
            azure_autoscaling = AKS("AKS")
            azure_elb = LoadBalancers("Load Balancer")

        with Group("Infrastructure"):
            azure_app_services = AppServices("App Services")
            azure_sqldatabases = SQLDatabases("SQL Database")
            azure_storage = StorageAccounts("Storage Account")

        azure_pipeline = Devops("Azure DevOps")

        azure_source >> azure_pipeline
        azure_pipeline >> azure_build >> azure_deploy >> azure_autoscaling
        azure_autoscaling >> azure_app_services
        azure_app_services >> azure_elb
        azure_sqldatabases >> azure_app_services
        azure_storage >> azure_app_services

