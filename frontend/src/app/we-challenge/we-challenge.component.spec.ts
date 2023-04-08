import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WeChallengeComponent } from './we-challenge.component';

describe('WeChallengeComponent', () => {
  let component: WeChallengeComponent;
  let fixture: ComponentFixture<WeChallengeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WeChallengeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WeChallengeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
