def get_ip(request):
    return request.scope.get("aws.event", {}).get("requestContext", {}).get("http", {}).get("sourceIp")