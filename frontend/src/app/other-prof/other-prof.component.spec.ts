import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OtherProfComponent } from './other-prof.component';

describe('OtherProfComponent', () => {
  let component: OtherProfComponent;
  let fixture: ComponentFixture<OtherProfComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OtherProfComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OtherProfComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
