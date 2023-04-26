import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Route, Router } from '@angular/router';
import { Post, PostsService } from '../posts.service';
import { Challenge, User } from '../models';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  private isLoggedin: Boolean | undefined;
  public user$: Observable<User> | undefined;
  public post: Post;
  public user: User | undefined;
  public challenge: Challenge | undefined;
  comment = this.formBuilder.group({
    comment: new FormControl(''),
  });
  
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

  constructor(private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private registrationService: RegistrationService,
    private challengeService: ChallengeService,
    private router: Router) {
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (this.isLoggedin) {
       // get current user information
      this.user$ = this.registrationService.getUserInfo();
      this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });
    }
    let data = route.snapshot.data as { post: Post };
    this.post = data.post;
    registrationService.getUser(this.post.user_id).subscribe(user => this.user = user)
    challengeService.getChallenge(this.post.challenge).subscribe(challenge => this.challenge = challenge)
    console.log(this.post.challenge)
  }

  ngOnInit() {
    
  }

  onSubmit(): void {
    let form = this.comment.value;
    let _c = form.comment ?? "";

    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    // get current user information
    this.user$ = this.registrationService.getUserInfo();
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });

    // this.registrationService
    // .loginUser(email, password)
    // .subscribe((response) => {
    //   const token = response as TokenResponse;
    //   if (token) {
    //     // Store the authentication token for future use
    //     localStorage.setItem('authToken', token.access_token);
    //     console.log(token)
    //     // Redirect the user to the home page
    //     window.location.reload();
    //     window.location.href = "/";
    //     /* this.router.navigate(['/']); */
    //   } else {
    //     // Handle the case where the login credentials are invalid
    //     console.error('Invalid credentials');
    //   }
    // });
  }
}
