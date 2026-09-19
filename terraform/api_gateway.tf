resource "aws_api_gateway_rest_api" "form_api" {
  name = "${var.project_name}-api"
}

resource "aws_api_gateway_resource" "form_endpoint" {
  parent_id = aws_api_gateway_rest_api.form_api.root_resource_id
  path_part = "submit"
  rest_api_id = aws_api_gateway_rest_api.form_api.id
}
