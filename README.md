# ReadAloudTweetByVoiceVox
twitterのタイムラインをVoiceVox使って読んでもらう

## 環境構築
- Mac
```
brew install pulseaudio
```
```
pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon
```
