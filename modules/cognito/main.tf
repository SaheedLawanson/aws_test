resource "aws_cognito_user_pool" "my_pool" {
    name = "my_pool"

    account_recovery_setting {
        recovery_mechanism {
            name = "verified_email"
            priority = 1
        }
    }

    auto_verified_attributes = ["email"]

    password_policy {
        minimum_length = 10
        require_lowercase = true
        require_numbers = true
        require_symbols = false
        require_uppercase = true     
    }

    schema {
        name = "email"
        attribute_data_type = "String"
        mutable = false
        required = true
    }

    schema {
        name = "phone_number"
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 14
        }
    }

    schema {
        name = "preferred_username" # last name
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    schema {
        name = "name" # full name
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    schema {
        name = "given_name" # first name
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    schema {
        name = "family_name" # last name
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    schema {
        name = "address"
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    schema {
        name = "gender" # last name
        attribute_data_type = "String"
        mutable = false
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    dynamic "schema" {
        for_each = var.attributes
        content {
            name = schema.value
            attribute_data_type = "String"
            string_attribute_constraints {
                min_length = 0
                max_length = 200
            }
        }
    }

    schema {
        name = "date_created"
        attribute_data_type = "String"
    }

    schema {
        name = "birthdate" # date of birth
        attribute_data_type = "String"
        required = true
        string_attribute_constraints {
            min_length = 0
            max_length = 200
        }
    }

    schema {
        name = "is_recurring"
        attribute_data_type = "Boolean"
    }

    schema {
        name = "account_number"
        attribute_data_type = "String"
        string_attribute_constraints {
            min_length = 0
            max_length = 10
        }
    }

    schema {
        name = "delete_flag"
        attribute_data_type = "Boolean"
    }

    schema {
        name = "last_logged_in"
        attribute_data_type = "String"
    }

    schema {
        name = "last_modified"
        attribute_data_type = "String"
    }

    schema {
        name = "bvn"
        attribute_data_type = "String"
        string_attribute_constraints {
            min_length = 0
            max_length = 14
        }
    }

    schema {
        name = "pin"
        attribute_data_type = "String"
        string_attribute_constraints {
            min_length = 0
            max_length = 14
        }
    }

    schema {
        name = "date_joined"
        attribute_data_type = "String"
    }

    schema {
        name = "is_superuser"
        attribute_data_type = "Boolean"
    }

    schema {
        name = "is_staff"
        attribute_data_type = "Boolean"
    }

    schema {
        name = "is_active"
        attribute_data_type = "Boolean"
    }

    schema {
        name = "receive_notification"
        attribute_data_type = "Boolean"
    }

    username_attributes = ["email"]
}

resource "aws_cognito_user_pool_client" "my_pool_client" {
    name = "my_pool_client"
    user_pool_id = aws_cognito_user_pool.my_pool.id

    explicit_auth_flows = [
        "USER_PASSWORD_AUTH"
    ]

    # generate_secret = true
}
