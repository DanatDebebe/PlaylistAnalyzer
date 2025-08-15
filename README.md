# Playlist Analyzer – Sentiment Analysis with Spotify API

**Status:** 🚫 Project Incomplete

## Overview

This project aimed to analyze the sentiment of tracks within a Spotify playlist using the Spotify Web API. My goal was to assess the emotional state of my friends based on the most recent playlist they made, but alas that wasnt possible.

## Challenges

As of late, Spotify introduced significant changes to their Web API, restricting access to several key endpoints necessary for this project. These changes include the deprecation of the `/recommendations`, `/audio-features`, and `/audio-analysis` endpoints, which are essential for analyzing track characteristics and generating personalized recommendations. :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

Consequently, the project's core functionality became unfeasible, as the required data could no longer be accessed through the API.:contentReference[oaicite:12]{index=12}

## Affected Endpoints

- `/v1/recommendations`
- `/v1/audio-features`
- `/v1/audio-analysis`

For detailed information on these changes, please refer to Spotify's official announcement: :contentReference[oaicite:13]{index=13}

## Conclusion

While the project could not be completed due to these unforeseen API restrictions, it highlights the challenges independent developers face when relying on third-party services that may alter their offerings without prior notice. AI paranoia is making the internet less fun :(


