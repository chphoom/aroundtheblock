import { Component } from '@angular/core';
import { Observable, map } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post, PostsService } from '../posts.service';
import { FormControl, FormGroup } from '@angular/forms';
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
  // uploadForm: FormGroup;
  public user: User | undefined;
  private isLoggedin: Boolean | undefined;
  challenge$: Observable<Challenge> | undefined;
  private challengeId: number | undefined;

  form = this.formBuilder.group({
    file: new FormControl(),
    title: '',
    description: '',
    private: [false]
  });

  constructor(private router: Router, private formBuilder: FormBuilder, challengeService: ChallengeService, private postsService: PostsService, private uploadService: UploadService, private registrationService: RegistrationService, private shareService: ShareService) {
/*     this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService */
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });

    this.registrationService.isAuthenticated$.subscribe(bool => this.isLoggedin = bool);
    if (!this.isLoggedin) {
      this.router.navigate(['/login'])
    }

    /* this.uploadForm = new FormGroup({
      file: new FormControl()
    }); */
  }

  onFileSelected(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('file')?.setValue(file);
    }
  }

  onSubmit() {
    console.log(this.form.value)
    
    const formData = new FormData();
    formData.append('file', this.form.get('file')?.value);
    const file = formData.get('file') as File;
    this.uploadService.uploadFile(formData).subscribe(response => {
      console.log(response);
    }, (error: HttpErrorResponse)=> {
      console.log(error);
    });

    this.challenge$ = this.shareService.getCurrentValue();
    this.challenge$.pipe(
      map(challenge => challenge.id)
    ).subscribe(id => {
      this.challengeId = id
    })

    let form = this.form.value

    const newPost: Post = {
      id: undefined,
      img: file.name,
      title: form.title ?? "Untitled",
      desc: form.description ?? "",
      private: form.private ?? false,
      created: new Date(),
      challenge: this.challengeId ?? 1,
      user_id: this.user!.email,
      comments: [],
      tags: []
    };

    console.log(newPost); 
    this.postsService.createPost(newPost).subscribe(response => {
      console.log(response);
    }, (error: HttpErrorResponse)=> {
      console.log(error);
    });
    // TODO: redirect to individual post page once that is created
    this.router.navigate(['/'])
  }
}
