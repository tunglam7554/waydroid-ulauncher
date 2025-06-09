#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
import os
import json
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

class WaydroidExtension(Extension):
    def __init__(self):
        super(WaydroidExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = [
            ExtensionResultItem(
                icon='images/start.png',
                name='Start Waydroid',
                description='Start the Waydroid container',
                on_enter=ExtensionCustomAction('start')
            ),
            ExtensionResultItem(
                icon='images/stop.png',
                name='Stop Waydroid',
                description='Stop the Waydroid container',
                on_enter=ExtensionCustomAction('stop')
            ),
            ExtensionResultItem(
                icon='images/restart.png',
                name='Restart Waydroid',
                description='Restart the Waydroid container',
                on_enter=ExtensionCustomAction('restart')
            ),
            ExtensionResultItem(
                icon='images/full-ui.png',
                name='Toggle Full UI',
                description='Toggle Waydroid full UI mode',
                on_enter=ExtensionCustomAction('full-ui')
            )
        ]
        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        command = event.get_data()
        
        if command == 'start':
            subprocess.Popen(['waydroid', 'session', 'start'])
        elif command == 'stop':
            subprocess.Popen(['waydroid', 'session', 'stop'])
        elif command == 'restart':
            subprocess.Popen(['waydroid', 'session', 'stop'])
            subprocess.Popen(['waydroid', 'session', 'start'])
        elif command == 'full-ui':
            subprocess.Popen(['waydroid', 'show-full-ui'])
            
        return HideWindowAction()

if __name__ == '__main__':
    WaydroidExtension().run() 