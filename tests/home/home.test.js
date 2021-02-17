import { act } from 'react-dom/test-utils';
import Home from '../../aginghub/home/home';
import React from 'react';
import { render, unmountComponentAtNode } from 'react-dom';

let container = null;
beforeEach(() => {
  container = document.createElement('div');
  document.body.appendChild(container);
});

afterEach(() => {
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

it('renders with welcome text', () => {
  act(() => {
    render(<Home />, container);
  });
  expect(container.textContent).toBe('Welcome to AgingHub');
});