# GTILE CONFIG #

import subprocess
from os import popen

from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart(): subprocess.Popen('/home/egsagon/.config/qtile/autostart.sh')

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    
    # Move windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    
    # Resise window
    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),
    
    # Start terminal
    Key([mod], "Return", lazy.spawn(terminal)),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    
    # Toggle floating
    Key([mod, 'shift'], 'space', lazy.window.toggle_floating()),
    
    # WM commands
    Key([mod,"shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "e", lazy.shutdown()),
    
    # Open rofi
    Key([mod], 'd', lazy.function(lambda *_: popen('/home/egsagon/.config/rofi/dmenu.sh'))),
    
    # Screenshot
    Key([mod, 'shift'], 's', lazy.function(lambda *_: popen('flameshot gui')))
]

groups = [Group(i) for i in "123456789"]

group_keys = [
    'ampersand',
    'eacute',
    'quotedbl',
    'apostrophe',
    'parenleft',
    'minus',
    'egrave',
    'underscore',
    'agrave',
]

for i, key in zip(groups, group_keys):
    keys.extend([Key([mod], key, lazy.group[i.name].toscreen()),
                 Key([mod, "shift"], key, lazy.window.togroup(i.name))])

layouts = [
    layout.Columns(border_focus_stack = ["#F00", "#0F0"],
                   border_focus = '#FF632F',
                   border_normal = '#FF632F',
                   border_on_single = True,
                   border_width = 3,
                   margin = 16)
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom = bar.Gap(80),
        wallpaper = '/home/egsagon/.bain/images/mars.png',
        wallpaper_mode = 'stretch',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        
        Match(title="glava")
    ],
    
    border_focus = '#FF632F',
    border_normal = '#FF632F',
    border_width = 3
)

auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = False
wl_input_rules = None

wmname = "i3" # LG3D qtile i3
