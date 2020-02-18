import numpy as np
import logging
from pathlib import Path
import copy

# CONSTANTS
# TODO : Possibly move to respective classes
_GHZ = 1.0
_MW_S1 = 'S1'  # disconnected for now
_MW_S2 = 'S2'  # channel 1, marker 1
_GREEN_AOM = 'Green'  # ch1, marker 2
_ADWIN_TRIG = 'Measure'  # ch2, marker 2
_CONN_DICT = {_MW_S1: None, _MW_S2: 1, _GREEN_AOM: 2, _ADWIN_TRIG: 4}
_PULSE_PARAMS = {
    'amplitude': 100, 'pulsewidth': 20, 'SB freq': 0.00, 'IQ scale factor': 1.0, 'phase': 0.0, 'skew phase': 0.0,
    'num pulses': 1
}


class SequenceEvent:
    """A single sequence event.

    :param event_type: The type of event.
    :param start: The start time of the event.
    :param stop: The stop time of the event.
    :param start_increment: The multiplier for incrementing the start time.
    :param stop_increment: The multiplier for incrementing the stop time.
    """

    def __init__(self, event_type, start, stop, start_increment=0, stop_increment=0):
        self.event_type = event_type
        self.start = start
        self.stop = stop
        self.start_increment = start_increment
        self.stop_increment = stop_increment

    def increment_time(self, dt=0):
        """Increments the start and stop times by dt.
        :param dt: The time increment.
        """

        self.start += dt * self.start_increment
        self.stop += dt * self.stop_increment


class Channel:
    """Provides functionality for a sequence of :class:`sequence events <SequenceEvent>`.

    :param seq: A collection of :class:`sequence events <SequenceEvent>`.
    :param delay: Delay in the format [AOM delay, MW delay].
    :param pulse_params: A dictionary containing parameters for the pulse, containing: amplitude, pulseWidth, SB frequency, IQ scale factor, phase, skewPhase.
    :param connection_dict: A dictionary of the connections between AWG channels and switches/IQ modulators.
    :param timeres: The clock rate in ns.
    """

    def __init__(self, seq, delay=[0, 0], pulse_params=None, connection_dict=None, timeres=1):
        self.logger = logging.getLogger('seqlogger.seq_class')
        self.seq = seq
        self.timeres = timeres
        self.delay = delay

        # init the arrays
        self.wavedata = None
        self.c1markerdata = None
        self.c2markerdata = None

        # set the maximum length to be zero for now
        self.maxend = 0

        if pulse_params is None:
            self.pulse_params = self._PULSE_PARAMS
        else:
            self.pulse_params = pulse_params

        if connection_dict is None:
            self.connection_dict = self._CONN_DICT
        else:
            self.connection_dict = connection_dict

    # TODO : Possibly make more self-explanatory function names
    def convert_pulse_params_from_dict(self):
        ssb_freq = float(self.pulseparams['SB freq']) * _GHZ  # SB freq is in units of GHZ
        iqscale = float(self.pulseparams['IQ scale factor'])
        phase = float(self.pulseparams['phase'])
        deviation = int(self.pulseparams['pulsewidth']) // self.timeres
        amp = int(self.pulseparams['amplitude'])  # needs to be a number between 0 and 100
        skew_phase = float(self.pulseparams['skew phase'])
        npulses = self.pulseparams['num pulses']
        return ssb_freq, iqscale, phase, deviation, amp, skew_phase, npulses

    def create_sequence(self, dt=0):
        """Creates the data for the sequence.

        :param dt: Increment in time.
        """

        # get the AOM delay
        aomdelay = int((self.delay[0] + self.timeres / 2) / self.timeres)  # proper way of rounding delay[0]/timeres
        self.logger.info("AOM delay is found to be %d", aomdelay)
        # get the MW delay
        mwdelay = int((self.delay[1] + self.timeres / 2) // self.timeres)
        self.logger.info("MW delay is found to be %d", mwdelay)

        # get all the pulse params
        ssb_freq, iqscale, phase, deviation, amp, skew_phase, npulses = self.convert_pulse_params_from_dict()

        # first increment the sequence by dt if needed
        for seq_event in self.seq:
            seq_event.increment_time(dt)

        # TODO : Start working here


class WaveEvent(SequenceEvent):
    """The abstract base class for a pulse event. Specific pulses (like Gaussian) should implement this class.

    :param wave_type: The type of wave being implemented.
    :param start: The start time of the event.
    :param stop: The stop time of the event.
    """
    WAVE_KEYWORD = "Wave"

    def __init__(self, wave_type, start, stop):
        super().__init__(self.WAVE_KEYWORD, start, stop)
        self.wave_type = wave_type

    def iq_generator(self, data):
        pass

    def data_generator(self):
        pass
