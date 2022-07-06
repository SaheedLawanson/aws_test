resource "aws_dynamodb_table" "my_table" {
    name = "my_table"
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "email"

    attribute {
      name = "email"
      type = "S"
    }
}