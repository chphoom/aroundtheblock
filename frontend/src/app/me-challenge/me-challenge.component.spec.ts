import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeChallengeComponent } from './me-challenge.component';

describe('MeChallengeComponent', () => {
  let component: MeChallengeComponent;
  let fixture: ComponentFixture<MeChallengeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MeChallengeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MeChallengeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
