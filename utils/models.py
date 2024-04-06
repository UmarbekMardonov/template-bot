nb = dict(null=True, blank=True)


def user_get_data(update):
    user_data = update.effective_user.to_dict()

    return dict(
        user_id=user_data["id"],
        **{
            k: user_data[k]
            for k in ["username", "first_name", "last_name", "language_code"]
            if k in user_data and user_data[k] is not None},
    )
