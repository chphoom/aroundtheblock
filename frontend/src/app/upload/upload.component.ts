import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Challenge, ChallengeService } from '../challenge.service';
import { Post, PostsService } from '../posts.service';
import { FormControl, FormGroup } from '@angular/forms';
import { UploadService } from '../upload.service';
import { HttpErrorResponse } from '@angular/common/http';
import { RegistrationService, User } from '../registration.service';
import { DateAdapter } from '@angular/material/core';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  uploadForm: FormGroup;
  public user: User | undefined;

  constructor(challengeService: ChallengeService, private postsService: PostsService, private uploadService: UploadService, private registrationService: RegistrationService) {
/*     this.current$ = challengeService.getCurrentChallenge()
    this.challengeService = challengeService */
    this.registrationService.getUserInfo().subscribe((user: User) => {
      this.user = user;
    });

    this.uploadForm = new FormGroup({
      file: new FormControl()
    });
  }

  onFileSelected(event: any) {

    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.uploadForm.get('file')?.setValue(file);
    }

    /* const file = event.target.files[0];
    this.uploadForm.patchValue({
      file: file
    }); */

  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.uploadForm.get('file')?.value);
    const file = formData.get('file') as File;
    this.uploadService.uploadFile(formData).subscribe(response => {
      console.log(response);
    }, (error: HttpErrorResponse)=> {
      console.log(error);
    });

    const newPost: Post = {
      id: 9,
      img: file.name,
      desc: "",
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
  }
}
