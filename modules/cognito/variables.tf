variable "attributes" {
    type = list(string)
    default = [
        "image_id", "profile_type",
        "balance", "tenant_id",
        "promo_code", "formatted_date",
        "father_name", "status", "city",
        "rating", "state",
        "country", "question_1",
        "question_2", "question_3",
        "answer_1", "answer_2",
        "answer_3", "docType",
        "countryCode"
    ]
}