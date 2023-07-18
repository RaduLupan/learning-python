import boto3

def lambda_handler(event, context):
    cluster_name = event['cluster_name']
    service_name = event['service_name']

    ecs_client = boto3.client('ecs')

    try:
        response = ecs_client.update_service(
            cluster=cluster_name,
            service=service_name,
            forceNewDeployment=True
        )
        print("Service redeployed successfully:", response)
    except Exception as e:
        print("Error redeploying service:", str(e))
