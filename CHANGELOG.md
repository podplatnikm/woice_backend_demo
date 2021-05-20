# Changelog
All notable changes to Porsche backend project will be documented in this file.

## Unreleased

##[0.1.4]() - 2021-05-20
### Added
- Private lobbies that users can invite other users to
- Messages in private lobbies are hidden from other users that are not a part of the private lobby
- Users can not join private lobbies if they are not owner or invited (and can not post messages)

##[0.1.3]() - 2021-05-20
### Added
- CRUD helpers from async
- WebSocket jwt authentication
- Users are now notified when someone else types
- Users can publish messages to lobbies
- Users can join existing lobbies

##[0.1.2]() - 2021-05-20
### Added
- ASGI server support
- In memory broker for channels

##[0.1.1]() - 2021-05-19
### Added
- Users can find, create and delete chat lobbies
- Users can find, update and delete lobby messages

##[0.1.0]() - 2021-05-19
### Added
- Verbose logging
- Custom user model for future extensions
- Swagger documentation
- JWT authentication

### Changed
- Updated README.md
