import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Route, Router } from '@angular/router';
import { Post, PostsService } from '../posts.service';
import { Challenge, User } from '../models';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { Observable, map, shareReplay } from 'rxjs';
import { MatSnackBar } from '@angular/material/snack-bar';
import { CommentService, Comment } from '../comment.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  public isLoggedin: Boolean | undefined;
  public user$: Observable<User> | undefined;
  public post: Post;
  public _user: User | undefined; // author of post
  public challenge: Challenge | undefined;
  public saved: { [key: number]: boolean } = {};
  public favorited: { [key: number]: boolean } = {};
  public user: User | undefined; // current user
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

  constructor(protected snackBar: MatSnackBar, private formBuilder: FormBuilder,
    private postsService: PostsService,
    private route: ActivatedRoute,
    private registrationService: RegistrationService,
    private challengeService: ChallengeService,
    private router: Router,
    private commentService: CommentService) {
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
    registrationService.getUser(this.post.user_id).subscribe(user => this._user = user)
    challengeService.getChallenge(this.post.challenge).subscribe(challenge => this.challenge = challenge)
    console.log(this.post.challenge)
    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
      user.savedChallenges?.forEach(challenge => {
        this.saved[challenge.id!] = !!user.savedChallenges?.find(chall => chall.id === challenge.id);
      });
      console.log(user);
      console.log(this.saved);
    });
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
      user.savedPosts?.forEach(post => {
        this.favorited[post.id!] = !!user.savedPosts?.find(post => post.id === post.id);
      });
      console.log(user);
      console.log(this.favorited);
    });
  }

  ngOnInit() {
    
  }

  save(c: Challenge) {
    this.registrationService.saveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user=user
      this.saved[c.id!] = !!user.savedChallenges?.find(chall => chall.id === c.id)
      console.log(this.saved);
      this.snackBar.open(`Challenge saved!`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  unsave(c: Challenge) {
    this.registrationService.unsaveChallenge(this.user!.email, c.id ?? 1).subscribe((user: User) => {
      console.log(user);
      this.user = user
      this.saved[c.id!] = !!user.savedChallenges?.find(chall => chall.id === c.id);
      console.log(this.saved);
      this.snackBar.open(`Challenge unsaved.`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  favorite(p: Post) {
    this.registrationService.savePost(this.user!.email, p.id ?? 1).subscribe((user: User) => {
      this.user=user
      this.favorited[p.id!] = !!user.savedPosts?.find(post => post.id === p.id)
      console.log(this.favorited);
      this.snackBar.open(`Post added to favorites!`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  unfavorite(p: Post) {
    this.registrationService.unsavePost(this.user!.email, p.id ?? 1).subscribe((user: User) => {
      this.user = user
      this.favorited[p.id!] = !!user.savedPosts?.find(post => post.id === p.id);
      console.log(this.favorited);
      this.snackBar.open(`Removed post from favorites.`, "", { duration: 2000 });
    }, (error) => {
      console.error(error);
    });
  }

  tagClick(tag: string) {
    window.location.reload();
    window.location.href = "/tagged/"+tag;
  }

  onComment(): void {
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

    this.commentService.createComment(_c, this.user!, this.post.id!)
      .subscribe((response) => {
          console.log(response)
          window.location.reload();
        }, (error) => {
          console.error(error);
        });

        console.log("LOOK HERE" + JSON.stringify(this.post.comments))
  }

  delComment(c: Comment): void {
    this.commentService.deleteComment(c).subscribe({
      next: (challenge) => {
        //update window
        window.location.reload();
      },
      error: (err) => { 
        if (err.message) {
          window.alert(err.message);
        } else {
          window.alert("Unknown error: " + JSON.stringify(err));
        }
      }
    })
  }

  private userCache: { [key: string]: Observable<string> } = {};

  getUsername(comment: Comment): Observable<string> {
    const cachedValue = this.userCache[comment.user_id];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registrationService.getUser(comment.user_id).pipe(
      map(user => user ? `${user.displayName}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache[comment.user_id] = newValue;
    return newValue;
  }

  private userCache2: { [key: string]: Observable<string> } = {};

  getPfp(comment: Comment): Observable<string> {
    const cachedValue = this.userCache2[comment.user_id];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registrationService.getUser(comment.user_id).pipe(
      map(user => user ? `${user.pfp}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache2[comment.user_id] = newValue;
    console.log("here" + newValue)
    return newValue;
  }

  delPost() {
    this.postsService.deletePost(this.post).subscribe({
      next: () => {
        
      },
      error: (err) => { 
        if (err.message) {
          window.alert(err.message);
        } else {
          window.alert("Unknown error: " + JSON.stringify(err));
        }
      }
    })
  }
}
