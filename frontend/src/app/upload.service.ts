import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  constructor(private http: HttpClient) {}

  uploadFile(formData: FormData) {
    return this.http.post('/api/uploadfile/', formData);
  }
}
