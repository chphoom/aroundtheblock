import { Component } from '@angular/core';
import { Observable, map } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post, PostsService } from '../posts.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpErrorResponse } from '@angular/common/http';
import { RegistrationService, User } from '../registration.service';
import { DateAdapter } from '@angular/material/core';
import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { ShareService } from '../share.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  public user: User | undefined;
  private isLoggedin: Boolean | undefined;
  challenge$: Observable<Challenge> | undefined;
  challenge: Challenge | undefined;
  post: Post | undefined;
  submitted = false;

  form = this.formBuilder.group({
    file: new FormControl('', Validators.required),
    title: '',
    description: '',
    private: [false]
  });

  constructor(private router: Router, private formBuilder: FormBuilder, challengeService: ChallengeService, private postsService: PostsService, private uploadService: UploadService, private registrationService: RegistrationService, private shareService: ShareService) {
    // check if user is authenticated
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });

    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }
    
    // check if there is a challenge and gets challenge
    this.challenge$ = this.shareService.getCurrentValue();
    this.challenge$.subscribe(challenge => this.challenge = challenge)
  }

  onFileSelected(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('file')?.setValue(file);
    }
  }

  onSubmit() {
    let form = this.form.value

    if (form.title == '') {
      form.title = "Untitled"
    }

    const newPost: Post = {
      id: undefined,
      img: form.file ?? "",
      title: form.title ?? "",
      desc: form.description ?? "",
      private: form.private ?? false,
      created: new Date(),
      challenge: this.challenge?.id ?? 1, // if no challenge, post to dummy challenge
      user_id: this.user!.email,
      comments: [],
      tags: []
    };

    if (this.challenge?.createdBy) {
      newPost.tags.push("meChallenge")
    } else {
      newPost.tags.push("weChallenge")
    }

    this.postsService.createPost(newPost).subscribe({
        next: (post) => this.onSuccess(post),
        error: (err) => this.onError(err)
    })
  }

  onSuccess(post: Post) {
    this.post = post
    this.router.navigate([`/post/${this.post?.id}`]);
  }

  onError(err: Error) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }

}
