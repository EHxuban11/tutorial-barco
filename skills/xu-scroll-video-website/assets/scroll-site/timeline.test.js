import test from 'node:test';
import assert from 'node:assert/strict';
import { sectionProgress, videoTime } from './timeline.js';
test('progress follows the sticky travel and clamps outside it',()=>{assert.equal(sectionProgress(100,3000,1000),0);assert.equal(sectionProgress(-1000,3000,1000),.5);assert.equal(sectionProgress(-2500,3000,1000),1);});
test('late metadata, invalid duration and final frame stay valid',()=>{assert.equal(videoTime(.7,NaN),0);assert.equal(videoTime(1,0),0);assert.ok(videoTime(1,6)<6);assert.equal(videoTime(0,6,2,4),2);assert.equal(videoTime(.5,6,2,4),3);assert.equal(videoTime(1,6,2,4),4);});
test('forward and backward scrubbing map reversibly to the same clip',()=>{const sequence=[0,.2,.9,.4,1,0];assert.deepEqual(sequence.map(p=>videoTime(p,12,1,11)),[1,3,10,5,11,1]);});
