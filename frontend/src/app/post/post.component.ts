import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Route } from '@angular/router';
import { Post, PostsService } from '../posts.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  public post: Post;
  
  public static Route: Route = {
    path: 'post/:id',
    component: PostComponent,
    resolve: {
      post: (route: ActivatedRouteSnapshot) => {
        const id = parseInt(route.paramMap.get('id')!);
        return inject(PostsService).getPost(id); 
    }
    }
  }

  constructor(private route: ActivatedRoute) {
    let data = route.snapshot.data as { post: Post };
    this.post = data.post;
  }

  ngOnInit() {
    
  }
}
