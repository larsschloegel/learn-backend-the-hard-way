def filter_messages(messages):
    filtered_messages = []
    dang_counts = []
    for message in messages:
        words = message.split()
        good_words = []
        dangs = []
        for word in words:
            if word == "dang":
                dangs.append(word)
            else:
                good_words.append(word)
        filtered_messages.append(" ".join(good_words))
        dang_counts.append(len(dangs))

    return filtered_messages, dang_counts
