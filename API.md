# API Documentation

Base URL: http://localhost:8000/api/

---

## Get All Documents

### Request

GET /api/documents/

### Response

```json
[
  {
    "id": 1,
    "title": "Linux Commands",
    "file": "/media/documents/linux.docx",
    "content": "...",
    "created_at": "2025-06-01T10:00:00Z"
  }
]
```

---

## Get Single Document

### Request

GET /api/documents/{id}/

### Example

GET /api/documents/1/

---

## Create Document

### Request

POST /api/documents/

Content-Type: multipart/form-data

### Parameters

| Name  | Type      | Required |
| ----- | --------- | -------- |
| title | string    | Yes      |
| file  | docx file | Yes      |

---

## Update Document

### Request

PUT /api/documents/{id}/

Content-Type: multipart/form-data

### Parameters

| Name  | Type      |
| ----- | --------- |
| title | string    |
| file  | docx file |

---

## Partial Update Document

### Request

PATCH /api/documents/{id}/

### Example

```json
{
  "title": "Updated Document Title"
}
```

Allows updating specific fields without re-uploading the document file.

---

## Delete Document

### Request

DELETE /api/documents/{id}/

---

## Ask Question

### Request

POST /api/documents/ask/

### Body

```json
{
  "question": "What is tar command?"
}
```

### Response

```json
{
  "answer": "tar is a Linux utility used for archiving files."
}
```

---

## Question History

### Request

GET /api/documents/history/

### Response

```json
[
  {
    "id": 1,
    "question": "What is tar command?",
    "answer": "tar is a Linux utility used for archiving files.",
    "created_at": "2025-06-01T10:00:00Z"
  }
]
```
