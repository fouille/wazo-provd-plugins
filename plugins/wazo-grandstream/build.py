# -*- coding: utf-8 -*-

# Copyright 2013-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

# Depends on the following external programs:
#  -rsync

from subprocess import check_call


@target('1.0.3.27', 'wazo-grandstream-1.0.3.27')
def build_1_0_3_27(path):
    check_call(
        [
            'rsync',
            '-rlp',
            '--exclude',
            '.*',
            '--include',
            '/templates/*',
            'common/',
            path,
        ]
    )

    check_call(['rsync', '-rlp', '--exclude', '.*', '1.0.3.27/', path])


@target('1.0.8.6', 'wazo-grandstream-1.0.8.6')
def build_1_0_8_6(path):
    check_call(
        [
            'rsync',
            '-rlp',
            '--exclude',
            '.*',
            '--include',
            '/templates/*',
            'common/',
            path,
        ]
    )

    check_call(['rsync', '-rlp', '--exclude', '.*', '1.0.8.6/', path])


@target('1.0.8.9', 'wazo-grandstream-1.0.8.9')
def build_1_0_8_9(path):
    check_call(
        [
            'rsync',
            '-rlp',
            '--exclude',
            '.*',
            '--include',
            '/templates/*',
            'common/',
            path,
        ]
    )

    check_call(['rsync', '-rlp', '--exclude', '.*', '1.0.8.9/', path])


@target('1.2.5.3', 'wazo-grandstream-1.2.5.3')
def build_1_2_5_3(path):
    check_call(
        [
            'rsync',
            '-rlp',
            '--exclude',
            '.*',
            '--include',
            '/templates/*',
            'common/',
            path,
        ]
    )

    check_call(['rsync', '-rlp', '--exclude', '.*', '1.2.5.3/', path])
