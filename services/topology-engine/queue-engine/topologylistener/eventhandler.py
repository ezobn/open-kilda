# Copyright 2017 Telstra Open Source
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import kafkareader
import json
import time
import threading

from messageclasses import MessageItem
from logger import get_logger


logger = get_logger()
logger.info('Topology engine started')
known_messages = ['switch', 'isl', 'port', 'flow_operation']
known_commands = ['flow_create', 'flow_delete', 'flow_update', 'flow_path',
                  'flow_get', 'flows_get', 'flow_reroute', 'network']


def get_events(thread_count):
    global workerthreadcount

    logger.info('starting thread: %s', str(thread_count))
    consumer = kafkareader.create_consumer()

    while True:
        try:
            raw_event = kafkareader.read_message(consumer)
            event = MessageItem(**json.loads(raw_event))

            if "TOPOLOGY_ENGINE" != event.destination:
                logger.debug('Skip message for %s', event.destination)
                continue

            if event.get_message_type() in known_messages\
                    or event.get_command() in known_commands:
                logger.debug('Processing message for %s', event.destination)
                t = threading.Thread(target=topology_event_handler,
                                     args=(event,))
                t.daemon = True
                t.start()

        except Exception as e:
            logger.exception(e.message)


def topology_event_handler(event):
    event_handled = False

    while not event_handled:
        event_handled = event.handle()

        if not event_handled:
            logger.error('Unable to process event: %s', event.get_type())
            logger.error('Message body: %s', event.to_json())
            time.sleep(.1)

    logger.debug('Event processed for: %s', event.get_type())
