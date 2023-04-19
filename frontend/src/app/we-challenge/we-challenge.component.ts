import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { UploadService } from '../upload.service';

@Component({
  selector: 'app-we-challenge',
  templateUrl: './we-challenge.component.html',
  styleUrls: ['./we-challenge.component.css']
})
export class WeChallengeComponent {
  uploadForm: FormGroup;

  constructor(private uploadService: UploadService) {
    this.uploadForm = new FormGroup({
      file: new FormControl()
    });
  }

  submit() {
    const formData = new FormData();
    formData.append('file', this.uploadForm.get('file')?.value);
    this.uploadService.uploadFile(formData).subscribe(response => {
      console.log(response);
    });
  }
}
