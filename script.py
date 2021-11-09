INTENTS = {
    "hello": {
        "prompt_name": "hello",
        "prompt_text": "{client_name}, добрый день! Вас беспокоит компания {company_name}, мы проводим опрос "
                       "удовлетворенности нашими услугами.  Подскажите, вам удобно сейчас говорить?",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз"),
        "handler": "handler_hello_logic",
        "scenario": {"NULL": "hello_null", "DEFAULT": "recommend_main", "confirm=true": "recommend_main",
                     "confirm=false": "hangup_wrong_time", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "hello_repeat"}
    },
    "hello_repeat": {
        "prompt_name": "hello_repeat",
        "prompt_text": "Это компания {company_name}. Подскажите, вам удобно сейчас говорить?",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз"),
        "handler": "handler_hello_logic",
        "scenario": {"NULL": "hello_null", "DEFAULT": "recommend_main", "confirm=true": "recommend_main",
                     "confirm=false": "hangup_wrong_time", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "hello_repeat"}
    },
    "hello_null": {
        "prompt_name": "hello_null",
        "prompt_text": "Извините, вас не слышно. Вы могли бы повторить",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз"),
        "handler": "handler_hello_logic",
        "scenario": {"NULL": "hangup_null", "DEFAULT": "recommend_main", "confirm=true": "recommend_main",
                     "confirm=false": "hangup_wrong_time", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "hello_repeat"}
    },
    "recommend_main": {
        "prompt_name": "recommend_main",
        "prompt_text": "Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, "
                       "по шкале от «0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую.",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative",
                     "wrong_time=true": "hangup_wrong_time", "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}
    },
    "recommend_repeat": {
        "prompt_name": "recommend_repeat",
        "prompt_text": "Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0 до 10,"
                       "где 0 - точно не порекомендую, 10 - обязательно порекомендую.",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "recommend_repeat_2": {
        "prompt_name": "recommend_repeat_2",
        "prompt_text": "Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, вы бы стали это "
                       "делать? Если «да» - то оценка «10», если точно нет – «0».",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "recommend_score_negative": {
        "prompt_name": "recommend_score_negative",
        "prompt_text": "Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7?",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "recommend_score_neutral": {
        "prompt_name": "recommend_score_neutral",
        "prompt_text": "Ну а от 0 до 10 как бы вы оценили?",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "recommend_score_positive": {
        "prompt_name": "recommend_score_positive",
        "prompt_text": "Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10?",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "recommend_null": {
        "prompt_name": "recommend_null",
        "prompt_text": "Извините вас свосем не слышно,  повторите пожалуйста?",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "hangup_null", "DEFAULT": "recommend_default",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "recommend_default": {
        "prompt_name": "recommend_default",
        "prompt_text": "повторите пожалуйста",
        "answer_phrase": ("NULL", "DEFAULT", "Да", "Нет", "Занят", "Еще раз", "0-8", "9-10", "Возможно", "Не знаю",
                          "Вопрос"),
        "handler": "handler_main_logic",
        "scenario": {"NULL": "recommend_null", "DEFAULT": "hangup_null",
                     "recommendation=positive": "recommend_score_positive",
                     "recommendation=negative": "recommend_score_negative", "wrong_time=true": "hangup_wrong_time",
                     "repeat=true": "recommend_repeat",
                     "recommendation_score=[0…8]": "hangup_negative", "recommendation_score=[9…10]": "hangup_positive",
                     "recommendation=neutral": "recommend_score_neutral",
                     "recommendation=dont_know": "recommend_repeat_2", "question=true": "forward"}

    },
    "hangup_positive": {
        "prompt_name": "hangup_positive",
        "prompt_text": "Отлично!  Большое спасибо за уделенное время! Всего вам доброго!",
        "answer_phrase": None,
        "handler": None,
        "scenario": "hangup_action"
    },
    "hangup_negative": {
        "prompt_name": "hangup_negative",
        "prompt_text": "Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго. ",
        "answer_phrase": None,
        "handler": None,
        "scenario": "hangup_action"
    },
    "hangup_wrong_time": {
        "prompt_name": "hangup_wrong_time",
        "prompt_text": "Извините пожалуйста за беспокойство. Всего вам доброго",
        "answer_phrase": None,
        "handler": None,
        "scenario": "hangup_action"
    },
    "hangup_null": {
        "prompt_name": "hangup_null",
        "prompt_text": "Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго",
        "answer_phrase": None,
        "handler": None,
        "scenario": "hangup_action"
    },
    "forward": {
        "prompt_name": "forward",
        "prompt_text": "Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. Пожалуйста оставайтесь на"
                       "линии.",
        "handler": None,
        "answer_phrase": None,
        "scenario": "bridge action"
    }
}