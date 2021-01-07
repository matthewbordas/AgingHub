const { merge } = require('webpack-merge');
const common = require('./webpack.common');

module.exports = merge(common, {
  devtool: 'inline-source-map',
  mode: 'development',
  devServer: {
    open: true,
    port: 8000,
    publicPath: 'localhost:8000/'
  }
});