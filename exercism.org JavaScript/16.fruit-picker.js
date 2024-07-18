

import { notify } from './notifier';
import { order } from './grocer';


export function onSuccess() {
  notify({ message: 'SUCCESS' });
}


export function onError() {
  notify({ message: 'ERROR' });
}


export function orderFromGrocer(query, onSuccessCallback, onErrorCallback) {
  order(query, onSuccess, onError);
}


export function postOrder(variety, quantity) {
  order({variety, quantity}, onSuccess, onError);
}


export function notify(message) {
  // This is a mocked function for use with the exercise.
  message;
}

export function order(query, onSuccess, onError) {
  // This is a mocked function for use with the exercise.
  query;
  onSuccess;
  onError;
}