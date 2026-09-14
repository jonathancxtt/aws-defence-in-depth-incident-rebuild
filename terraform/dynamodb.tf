resource "aws_dynamodb_table" "submissions" {
    name = "${var.project_name}-submissions"
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "submission_id"
    attribute {
        name = "submission_id"
        type = "S"
    }
    tags = {
        Name = "${var.project_name}-submissions"
    }
}