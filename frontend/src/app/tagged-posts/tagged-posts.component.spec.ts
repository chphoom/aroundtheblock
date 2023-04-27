import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TaggedPostsComponent } from './tagged-posts.component';

describe('TaggedPostsComponent', () => {
  let component: TaggedPostsComponent;
  let fixture: ComponentFixture<TaggedPostsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TaggedPostsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TaggedPostsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
