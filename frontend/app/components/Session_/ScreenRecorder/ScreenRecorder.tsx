import React from 'react';
import { screenRecorder } from 'App/utils/screenRecorder';
import { Tooltip } from 'react-tippy';
import { connect } from 'react-redux';
import { Button } from 'UI';
import { requestRecording, stopRecording, connectPlayer } from 'Player';
import { SessionRecordingStatus } from 'Player/MessageDistributor/managers/AssistManager';
let stopRecorderCb: () => void;
import { recordingsService } from 'App/services';
import { toast } from 'react-toastify';

/**
 * "edge" || "edg/"   chromium based edge (dev or canary)
 * "chrome" && window.chrome   chrome
 * "opr" && (!!window.opr || !!window.opera)   opera
 * "trident"   ie
 * "firefox"   firefox
 * "safari"   safari
 */
function isSupported() {
  const agent = window.navigator.userAgent.toLowerCase();

  if (agent.includes('edge') || agent.includes('edg/')) return true;
  // @ts-ignore
  if (agent.includes('chrome') && !!window.chrome) return true;

  return false;
}

const supportedBrowsers = ['Chrome v91+', 'Edge v90+'];
const supportedMessage = `Supported Browsers: ${supportedBrowsers.join(', ')}`;

function ScreenRecorder({
  recordingState,
  siteId,
  sessionId,
}: {
  recordingState: SessionRecordingStatus;
  siteId: string;
  sessionId: string;
}) {
  const [isRecording, setRecording] = React.useState(false);

  React.useEffect(() => {
    return () => stopRecorderCb?.();
  }, []);

  const onSave = async (saveObj: { name: string; duration: number }, blob: Blob) => {
    try {
      const url = await recordingsService.reserveUrl(siteId, saveObj);
      const status = recordingsService.saveFile(url, blob);

      if (status) {
        toast.success('Session recording saved');
      }
    } catch (e) {
      console.error(e);
    }
  };

  React.useEffect(() => {
    if (!isRecording && recordingState === SessionRecordingStatus.Recording) {
      startRecording();
    }
    if (isRecording && recordingState !== SessionRecordingStatus.Recording) {
      stopRecordingHandler();
    }
  }, [recordingState, isRecording]);

  const startRecording = async () => {
    const stop = await screenRecorder('test rec_' + new Date().getTime(), sessionId, onSave);
    stopRecorderCb = stop;
    setRecording(true);
  };

  const stopRecordingHandler = () => {
    stopRecording();
    stopRecorderCb?.();
    setRecording(false);
  };

  const recordingRequest = () => {
    requestRecording();
    // startRecording()
  };

  if (!isSupported())
    return (
      <div className="p-2">
        {/* @ts-ignore */}
        <Tooltip title={supportedMessage}>
          <Button icon="record-circle" disabled variant={isRecording ? 'text-red' : 'text-primary'}>
            Record Activity
          </Button>
        </Tooltip>
      </div>
    );
  return (
    <div onClick={!isRecording ? recordingRequest : stopRecordingHandler} className="p-2">
      <Button
        icon={!isRecording ? 'stop-record-circle' : 'record-circle'}
        variant={isRecording ? 'text-red' : 'text-primary'}
      >
        {isRecording ? 'Stop Recording' : 'Record Activity'}
      </Button>
    </div>
  );
}

export default connectPlayer((state: any) => ({ recordingState: state.recordingState }))(
  connect((state: any) => ({
    siteId: state.getIn(['site', 'siteId']),
    sessionId: state.getIn(['sessions', 'current', 'sessionId']),
  }))(ScreenRecorder)
);