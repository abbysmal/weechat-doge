#!/bin/env python2
# -*- coding: utf-8 -*-

"""
This modules implement a doge-things-throwing function for weechat.
"""

import weechat
from random import shuffle

weechat.register('DogeSay', 'Lamagicien', '0.1', 'GPL3', '', '', '')
weechat.prnt('', 'Much scripting, such good devops, wow DogeSay loaded')

TOKENS = ['wow', 'such', 'much', 'so', 'very']


def doge_cb(data, buf, args):
    """
    This function take some shit and then throw some doge-things in weechat.
    """
    words = args.split(' ')
    if len(words) < 2 or len(words) > len(TOKENS):
        weechat.prnt('', 'Error, much sadness :(')
        return weechat.WEECHAT_RC_ERROR
    random_tokens = TOKENS[:]
    shuffle(random_tokens)
    dogefied = ['{} {}'.format(token, word)
                for token, word in zip(random_tokens[:len(words)], words)]
    weechat.command(weechat.current_buffer(), ', '.join(dogefied))
    return weechat.WEECHAT_RC_OK

weechat.hook_command(
    'dogesay',
    'Much doge, such amaze',
    'You need two to five words to start being doge',
    '',
    '',
    'doge_cb',
    ''
)
#  vim: set tabstop=4 shiftwidth=4 expandtab autoindent :
