import weechat
from random import shuffle

weechat.register('DogeSay', 'Lamagicien', '0.1', 'GPL3', '', '', '')
weechat.prnt('', 'Much scripting, such good devops, wow DogeSay loaded')


def doge_cb(data, buf, args):
    words = args.split(' ')
    if len(words) < 2 or len(words) > 5:
        weechat.prnt('', 'Error, much sadness :(')
        return (weechat.WEECHAT_RC_ERROR)
    tokens = ['wow', 'such', 'much', 'so', 'very']
    shuffle(tokens)
    dogefied = [tokens.pop() + ' {}'.format(word) for word in words]
    weechat.command(weechat.current_buffer(), ', '.join(dogefied))
    return (weechat.WEECHAT_RC_OK)


weechat.hook_command('dogesay', 'Much doge, such amaze', 'You need two to five words to start being doge', '', '', 'doge_cb', '')
