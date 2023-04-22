import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post, PostsService } from '../posts.service';
import { FormControl, FormGroup } from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpErrorResponse } from '@angular/common/http';
import { RegistrationService, User } from '../registration.service';
import { DateAdapter } from '@angular/material/core';
import { Router } from '@angular/router';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  // uploadForm: FormGroup;
  public user: User | undefined;
  private isLoggedin: Boolean | undefined;

  form = this.formBuilder.group({
    file: new FormControl(),
    title: '',
    description: '',
  });

  constructor(private router: Router, private formBuilder: FormBuilder, challengeService: ChallengeService, private postsService: PostsService, private uploadService: UploadService, private registrationService: RegistrationService) {
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

    const newPost: Post = {
      id: undefined,
      img: file.name,
      desc: this.form.value.description ?? "",
      private: false,
      created: new Date(),
      challenge: 1,
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
    this.router.navigate(['/we-challenge'])
  }

  ngOnInit() {
    
  }
}
