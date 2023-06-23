import re
import longfile as long
def message_probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_words=True
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1
    percentage= float(message_certainty)/ float(len(recognised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words= False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
def check_all_messages(message):
    highest_prob_list = {}
    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)
    response('Hello!',['hello','hi','yo','sup','hey','heyo'],single_response=True)
    response('I\'m doing fine thanks for asking , what about you?',['how','are','you','doing'],required_words=['how'])
    response('thank you !',['i', 'love','your','responses'],required_words=['love','ypur','responses'])
    response(long.R_EATING,['what', 'you', 'eat'],required_words=['you','eat'])
    response('My name is deepika ',['what','is','your','name'],required_words=['what', 'name'])
    response('I am sorry  ',['you','are','useless'],required_words=['you','useless']) 

    best_match=max(highest_prob_list,key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match]<1else best_match
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Bot:' + get_response(input('you:')))
