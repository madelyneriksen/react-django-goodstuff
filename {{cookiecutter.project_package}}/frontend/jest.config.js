module.exports = {
  // Mock all extras.
  "moduleNameMapper": {
    ".+\\.(css|styl|less|sass|scss)$": "identity-obj-proxy",
    ".+\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|yaml|yml|m4a|aac|oga)$": "<rootDir>/__mocks__/fileMock.js"
  },
  "setupFilesAfterEnv": ["<rootDir>/src/setupTests.js"],
}
