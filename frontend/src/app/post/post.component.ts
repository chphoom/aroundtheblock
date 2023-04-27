import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, Route } from '@angular/router';
import { Post, PostsService } from '../posts.service';
import { Challenge, User } from '../models';
import { RegistrationService } from '../registration.service';
import { ChallengeService } from '../challenge.service';
import { Observable } from 'rxjs';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  public post: Post;
  public _user: User | undefined;
  public challenge: Challenge | undefined;
  public saved: { [key: number]: boolean } = {};
  public user: User | undefined;
  public isLoggedin: Boolean | undefined;

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

  constructor(protected snackBar: MatSnackBar, private route: ActivatedRoute, private registrationService: RegistrationService, private challengeService: ChallengeService) {
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

  tagClick(tag: string) {
    // Redirect the user to the home page
    window.location.reload();
    window.location.href = "/tagged/"+tag;
  }
}
