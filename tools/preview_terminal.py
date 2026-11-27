#!/usr/bin/env python3
"""Export actual terminal components at wide/narrow sizes, without changing progress."""
import io
import os
from pathlib import Path
import sys
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from course import engine, terminal as ui


def main():
    if ui.BACKEND=='plain':
        raise SystemExit('Rich is needed for preview export. Run ./learn setup.')
    # A preview explicitly requests color; do not change the calling shell's preferences.
    os.environ.pop('NO_COLOR',None)
    ui.configure('always')
    build=engine.ROOT/'.build/previews'
    build.mkdir(parents=True,exist_ok=True)
    state=engine.load_state()
    for width in (96,52):
        output=io.StringIO()
        console=ui.console(output,record=True,width=width)
        with patch.object(ui,'console',return_value=console):
            engine.status(state)
            ui.menu()
            ui.panel('YOUR WORKBENCH','Restore a simulated receiver, one tested component at a time.\n'
                     'Start here: ./learn lesson 1')
            ui.syntax('#include <stdint.h>\n\n// Every sample has a format, a rate, and an owner.\n'
                      'uint32_t sample_rate_hz = 1000000;\nint16_t in_phase = 8192;\n', 'c')
        path=build/f'terminal-{width}.svg'
        console.save_svg(str(path),title='Signal Station / RFMastery')
        print(path)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
