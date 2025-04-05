import os
from PyPDF2 import PdfReader

def extract_pdf_content(pdf_path):
    """PDF 파일에서 텍스트 내용을 추출합니다."""
    try:
        print(f"PDF 파일 경로: {os.path.abspath(pdf_path)}")
        reader = PdfReader(pdf_path)
        text = ""
        
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- 페이지 {i+1} ---\n{page_text}"
        
        return text
    except Exception as e:
        print(f"PDF 파일 처리 중 오류 발생: {str(e)}")
        return None

def main():
    pdf_path = "250402_H10 사용설명서.pdf"
    if not os.path.exists(pdf_path):
        print(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")
        return
    
    pdf_content = extract_pdf_content(pdf_path)
    if pdf_content:
        output_file = "pdf_content.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(pdf_content)
        print(f"PDF 내용이 {output_file}에 저장되었습니다.")
        
        # 텍스트 일부 미리보기
        print("\n내용 미리보기:")
        preview = pdf_content[:1000] if len(pdf_content) > 1000 else pdf_content
        print(preview)

if __name__ == "__main__":
    main() 